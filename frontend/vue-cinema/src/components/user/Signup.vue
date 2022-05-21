<template>
  <div class="signup">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign up</h1>
      </div>
    </div>

    <section class="section">
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
                  <input type="text" class="input" v-model="birth_date" />
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
      password2: "",
      email: "",
      first_name: "",
      last_name: "",
      birth_date: null,
      errors: [],
    };
  },
  mounted() {
    document.title = "Sign up";
  },
  methods: {
    submitForm() {
      console.log("submitForm");
      console.log(this.username, this.last_name, this.first_name, this.email, this.birth_date)

      this.errors = [];
      if (this.first_name === "") {
        this.errors.push("The first_name is missing!");
      }
      if (this.last_name === "") {
        this.errors.push("The last_name is missing!");
      }
      if (this.username === "") {
        this.errors.push("The username is missing!");
      }

      if (this.password === "") {
        this.errors.push("The password is missing!");
      }

      if (this.password !== this.password2) {
        this.errors.push("The passwords are not matching!");
      }
      

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
  },
};
</script>
