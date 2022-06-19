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
    <section class=" bg-image">
      <div class="mask d-flex align-items-center gradient-custom-3">
        <div class="container ">
          <div class="row d-flex justify-content-center align-items-center">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px;margin-bottom: 2rem;">
                <div class="card-body p-5">
                  <h2 class="text-uppercase text-center mb-5">Авторизация</h2>
                  <!-- <div class="col-sm-12 m-1 text-center " v-if='errors'>
                    <div class="alert alert-warning" role="alert">
                      {{ errors }}
                    </div>
                  </div> -->
                
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
