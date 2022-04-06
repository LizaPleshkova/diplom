<template>
  <div class="mx-auto text-center">
    <form class="form-signin mx-auto" v-on:submit.prevent="submitForm">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>

      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">
          {{ error }}
        </p>
      </div>

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
      <button class="btn btn-lg btn-primary btn-block" type="submit">
        Sign in
      </button>
      <p class="mt-5 mb-3 text-muted">
        Or <router-link to="/sign-up">click here</router-link> to sign up!
      </p>
    </form>
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

      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing!");
      }

      if (this.password === "") {
        this.errors.push("The password is missing!");
      }

      if (!this.errors.length) {
        // const formData = {
        //     username: this.username,
        //     password: this.password
        // }

        axios({
          method: "post",
          url: "http://localhost:8000/client/api/token/",
          data: {
            username: this.username,
            password: this.password,
          },
          credentials: "include",
        })
          .then((response) => {
            const accessToken = response.data.access;
            // const refreshToken = response.data.refresh
            console.log(response.data);
            this.$store.commit("setToken", accessToken);
            axios.defaults.headers.common["Authorization"] =
             'Bearer ' + accessToken;

            localStorage.setItem("token", accessToken);
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
