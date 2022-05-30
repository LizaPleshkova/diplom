from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_superuser', 'birth_date')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'birth_date')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if type(attrs['birth_date']) != type(''):
            print('here', attrs['birth_date'])
            # datetime_birth = parse(attrs['birth_date'])
            print(attrs['birth_date'], type(attrs['birth_date']))
            datetime_birth = attrs['birth_date'].strftime('%Y-%m-%d')
            # datetime_birth = datetime.strptime(attrs['birth_date'], "%Y-%m-%d").date()
            attrs['birth_date'] = datetime_birth
            print(datetime_birth)
        else:
            raise serializers.ValidationError({"birth_date": "Something wrong with date type"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birth_date=validated_data['birth_date']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
