<template>
  <div class="container">
    <div class="row col-8 justify-content-center">
      <div class="mx-auto text-center">
        <form class="form-signin mx-auto" v-on:submit.prevent="submitForm">
          <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>

          <label for="inputLogin" class="sr-only">Username</label>
          <input
            type="text"
            id="inputLogin"
            v-model="username"
            name="username"
            class="m-2 form-control form-outline mb-4"
            placeholder="Login"
            required=""
            autofocus=""
          />
          <label for="inputPassword" class="sr-only">Password</label>
          <input
            type="password"
            id="inputPassword"
            v-model="password"
            name="password"
            class="m-2 form-control"
            placeholder="Password"
            required=""
          />
          <button class="btn button btn-lg btn-primary btn-block" type="submit">
            Sign in
          </button>
          <p class="mt-5 mb-3 text-muted">
            Or <router-link to="/signup/">click here</router-link> to sign up!
          </p>
        </form>
      </div>
    </div>
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
