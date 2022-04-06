<template>
  <div class="login">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log in</h1>
      </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <form v-on:submit.prevent="submitForm">
                        <div class="field">
                            <label>Name</label>
                            <div class="control">
                            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
                            </div>
                        </div>

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="password" class="input" v-model="password">
                            </div>
                        </div>

                        <div class="notification is-danger" v-if="errors.length">
                            <p
                                v-for="error in errors"
                                v-bind:key="error"
                            >
                                {{ error }}
                            </p>
                        </div>

                        <div class="field">
                            <div class="control">
                                <button class="button is-dark">Log in</button>
                            </div>
                        </div>
                    </form>

                    <hr>

                    Or <router-link to="/sign-up">click here</router-link> to sign up!
                </div>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log in'
    },
    methods: {
        submitForm() {
            console.log('submitForm')

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing!')
            }

            if (this.password === '') {
                this.errors.push('The password is missing!')
            }

            if (!this.errors.length) {
                // const formData = {
                //     username: this.username,
                //     password: this.password
                // }

                axios({
                        method: 'post',
                        url: 'http://localhost:8000/client/api/token/',
                        data: {
                            username: this.username,
                            password: this.password
                        },
                        credentials: 'include',
                    }).then((response) => {
                        const accessToken = response.data.access
                        // const refreshToken = response.data.refresh
                        console.log(response.data);
                        this.$store.commit('setToken', accessToken)
                        axios.defaults.headers.common['Authorization'] = "Token " + accessToken

                        localStorage.setItem('token', accessToken)
                        this.$router.push('/')
                    })
                    .catch(err => {
                        console.log(err)
                    })
            }
        }
    }
}
</script>