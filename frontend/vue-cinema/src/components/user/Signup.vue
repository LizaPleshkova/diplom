<template>
  <div class="signup">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <!-- <h1 class="title">Sign up</h1> -->
      </div>
    </div>
    <div class="col-sm-12 m-1 text-center " v-if='errors.length'>
      <div class="alert alert-warning" role="alert">
        {{ errors }}
      </div>
    </div>
    <section class=" bg-image">
      <div class="mask d-flex align-items-center gradient-custom-3">
        <div class="container">
          <div class="row d-flex justify-content-center align-items-center">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px; margin: 2rem;">
                <div class="card-body p-5">
                  <h3 class="text-uppercase text-center mb-5">Создай аккаунт</h3>
                  <!-- <div class="col-sm-12 m-1 text-center " v-if='errors'>
        <div class="alert alert-warning" role="alert">
          {{ errors }}
        </div>
      </div> -->
                  <form v-on:submit.prevent="submitForm">

                    <div class="form-outline mb-4">
                      <input type="text" id="username" class="form-control form-control-lg" placeholder="Логин"
                        v-model="username" />
                      <!-- <label class="form-label" for="username">Your nick</label> -->
                    </div>

                    <div class="form-outline mb-4">
                      <input type="text" id="first_name" class="form-control form-control-lg" placeholder="Имя"
                        v-model="first_name" />
                      <!-- <label class="form-label" for="first_name">Your First Name</label> -->
                    </div>


                    <div class="form-outline mb-4">
                      <input type="text" id="last_name" class="form-control form-control-lg" placeholder="Фамилия"
                        v-model="last_name" />
                      <!-- <label class="form-label" for="last_name">Your Last Name</label> -->
                    </div>

                    <div class="form-outline mb-4">
                      <input type="email" id="email" class="form-control form-control-lg" placeholder="Почта"
                        v-model="email" />
                      <!-- <label class="form-label" for="email">Your Email</label> -->
                    </div>


                    <div class="form-outline mb-4">
                      <input type="text" id="birth_date" class="form-control form-control-lg"
                        placeholder="Дата рождения в формате: YYYY-MM-DD" v-model="birth_date" />
                      <!-- <label class="form-label" for="birth_date">Your birth_date</label> -->
                    </div>

                    <div class="form-outline mb-4">
                      <input type="password" id="password" class="form-control form-control-lg" placeholder="Пароль"
                        v-model="password" />
                      <!-- <label class="form-label" for="password">Password</label> -->
                    </div>

                    <div class="form-outline mb-4">
                      <input type="password" id="password2" class="form-control form-control-lg"
                        placeholder="Повтори пароль" v-model="password2" />
                      <!-- <label class="form-label" for="password2">Repeat your password</label> -->
                    </div>

                    <div class="d-flex justify-content-center">
                      <button type="submit" value="submit" style=" margin-top: 2rem;"
                        class="btn btn-success btn-block btn-lg gradient-custom-4 text-body">Зарегистрироваться</button>
                    </div>

                    <p class="text-center text-muted mt-5 mb-0">Уже есть аккаунт? <u>
                        <router-link to="/login/">Войти в систему</router-link>
                      </u></p>

                  </form>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form v-on:submit.prevent="submitForm">

            <div class="field">
                <label>Username</label>
                <div class="control">
                  <input type="text" class="input" v-model="username" />
                </div>
              </div>
              <div class="field">
                <label>First name</label>
                <div class="control">
                  <input type="text" class="input" v-model="first_name" />
                </div>
              </div>
              <div class="field">
                <label>Last name</label>
                <div class="control">
                  <input type="text" class="input" v-model="last_name" />
                </div>
              </div>
              <div class="field">
                <label>Email</label>
                <div class="control">
                  <input type="email" class="input" v-model="email" />
                </div>
              </div>
<div class="field">
                <label>Birth date</label>
                <div class="control">
                  <input type="text" class="input" placeholder="YYYY-MM-DD"  v-model="birth_date" />
                </div>
              </div>
              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password" />
                </div>
              </div>

              <div class="field">
                <label>Repeat password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password2" />
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">
                  {{ error }}
                </p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-dark">Sign up</button>
                </div>
              </div>
            </form>

            <hr />

            Or <router-link to="/login/">click here</router-link> to log in!
          </div>
        </div>
      </div>
    </section> -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      email: "",
      first_name: "",
      last_name: "",
      birth_date: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Sign up";
  },
  methods: {
    checkForm: function () {
      this.errors = [];
      var letters_re = /^[а-яА-ЯёЁa-zA-Z]+$/;
      letters_re.test(this.login);

      if (this.first_name === "") {
        this.errors.push("Укажите имя");
      } else if(letters_re.test(this.first_name)){
       this.errors.push('Укажите имя в корректном формате');
      }
      if (this.last_name === "") {
        this.errors.push("Укажите фамилию");
      }else if(letters_re.test(this.first_name)){
       this.errors.push('Укажите фамилию в корректном формате');
      }
      if (this.username === "") {
        this.errors.push("Укажите логин");
      } else if (!this.validLogin(this.username) && this.username.length < 8) {
        this.errors.push('Укажите корректный логин.');
      }
      if (!this.email) {
        this.errors.push("Укажите адрес электронной почты");
      } else if (!this.validEmail(this.email)) {
        this.errors.push('Укажите корректный адрес электронной почты.');
      }

      if (this.password === "") {
        this.errors.push("Укажите пароль");
      }

      if (this.password !== this.password2) {
        this.errors.push("Пароли не совпадают");
      }


      if (!this.errors.length) {
        return true;
      }
    },
    submitForm() {
      console.log("submitForm");
      console.log(this.username, this.last_name, this.first_name, this.email, this.birth_date)

      // this.errors = [];
      // if (this.first_name === "") {
      //   this.errors.push("The first_name is missing!");
      // }
      // if (this.last_name === "") {
      //   this.errors.push("The last_name is missing!");
      // }
      // if (this.username === "") {
      //   this.errors.push("The username is missing!");
      // }
      // if (!this.email) {
      //   this.errors.push("The username is missing!");
      // } else if (!this.validEmail(this.email)) {
      //   this.errors.push('Укажите корректный адрес электронной почты.');
      // }

      // if (this.password === "") {
      //   this.errors.push("The password is missing!");
      // }

      // if (this.password !== this.password2) {
      //   this.errors.push("The passwords are not matching!");
      // }
      if(!this.checkForm()){
        console.log('smth wrong')
        return;
      }
      console.log(this.birth_date, typeof (this.birth_date))
      if (!this.errors.length) {
        axios({
          method: "post",
          url: `http://localhost:8000/client/register/`,
          data: {
            username: this.username,
            password: this.password,
            password2: this.password2,
            email: this.email,
            first_name: this.first_name,
            last_name: this.last_name,
            // birth_date: new Date(this.birth_date).toISOString(),
            birth_date: this.birth_date,
          },
          credentials: "include",
        })
          .then((response) => {
            console.log('from reg comp', response.data);
            this.$router.push("/login/");
          })
          .catch((err) => {
            console.log(err);
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }

              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
    validEmail: function (email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    validLogin: function (login) {
      var re = /^[a-zA-Z][a-zA-Z0-9-_\.]{2,20}$/;
      return re.test(login);
    },
  },
};
</script>
