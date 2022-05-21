from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dateutil.parser import parse

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

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    birth_date = serializers.DateField()

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

        if type(attrs['birth_date']) == type(''):
            datetime_birth = parse(attrs['birth_date'])
            attrs['birth_date'] = datetime_birth.date()
            print(datetime_birth)
        else:
            raise serializers.ValidationError({"birth_date": "Something wrong with date type"})
        return attrs

    def to_internal_value(self, data):
        datas = super().to_internal_value(data)
        print(datas)
        datetime_birth = parse(datas['birth_date'])
        datas['birth_date'] = datetime_birth
        print(datetime_birth)
        return data

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
