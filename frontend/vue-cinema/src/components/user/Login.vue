<template>
  <div class="container">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <!-- <h1 class="title">Авторизация</h1> -->
      </div>
    </div>
    <div class="col-sm-12 m-1 text-center " v-if='errors.length'>
      <div class="alert alert-warning" role="alert">
        {{ errors }}
      </div>
    </div>
    <section class="vh-100 bg-image">
      <div class="mask d-flex align-items-center h-100 gradient-custom-3">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px;">
                <div class="card-body p-5">
                  <h2 class="text-uppercase text-center mb-5">Авторизация</h2>
                  <div class="col-sm-12 m-1 text-center " v-if='errors'>
                    <div class="alert alert-warning" role="alert">
                      {{ errors }}
                    </div>
                  </div>
                  <form v-on:submit.prevent="submitForm">

                    <div class="form-outline mb-4">
                      <input type="text" id="username" class="form-control form-control-lg" v-model="username"
                        placeholder="логин" />
                      <!-- <label class="form-label" for="username">Твой ник</label> -->
                    </div>

                    <div class="form-outline mb-4">
                      <input type="password" id="password" class="form-control form-control-lg" v-model="password"
                        placeholder="пароль" />
                      <!-- <label class="form-label" for="password">Пароль</label> -->
                    </div>

                    <button class="btn btn-success btn-block btn-lg gradient-custom-4 text-body" type="submit">
                      Войти
                    </button>
                    <p class="text-center text-muted mt-5 mb-0">
                      Или нажми<router-link to="/signup/"> здесь</router-link>, чтобы зарегистрироваться!
                    </p>
                  </form>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Log in";
  },
  methods: {
    submitForm() {
      console.log("submitForm");

      // axios.defaults.headers.common["Authorization"] = "";

      // localStorage.removeItem("token");
      // localStorage.removeItem("refreshToken");

      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing!");
      }

      if (this.password === "") {
        this.errors.push("The password is missing!");
      }

      if (!this.errors.length) {
        axios({
          method: "post",
          url: `http://localhost:8000/client/api/token/`,
          data: {
            username: this.username,
            password: this.password,
          },
          credentials: "include",
        })
          .then((response) => {
            console.log("fomr login vue", response);

            const accessToken = response.data.access;
            const refreshToken = response.data.refresh;

            console.log("tokens ", accessToken, refreshToken);
            // const refreshToken = response.data.refresh
            this.$store.commit("setToken", accessToken, refreshToken);

            localStorage.setItem("token", accessToken);
            localStorage.setItem("refreshToken", refreshToken);

            this.$router.push("/");
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>
