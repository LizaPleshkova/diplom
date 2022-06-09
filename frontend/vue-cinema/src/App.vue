<template>

  <div id="#app">
    <Header />
    <div id="page" class="page">
      <!-- mian-content -->
      <!-- <div class="main-banner bg bg1" id="home" style="
          background-color: rgba(0, 0, 0, 0);
          margin-top: 0px;
          background-image: url('/static/try4.jpg');
        ">
        <div class="banner-info">
          <p class="editContent">for booking</p>
          <h3 class="mb-4 editContent">Cinema</h3>
        </div>
      </div> -->
    </div>
    <!-- <ol class="breadcrumb editContent">
      <li class="breadcrumb-item">
        <a href="#" class="editContent">Home</a>
      </li>
    </ol> -->
    <section class="ab-info-main editContent" style="padding-left: 1rem; padding-right: 1rem">
      <div class="container-fluid py-md-3">
        <router-view />
      </div>
    </section>
    <Footer />
  </div>

</template>

<script>
import Header from "./components/base/Header";
import Footer from "./components/base/Footer";
import axios from 'axios';


export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    console.log(this.$store.state.authModule.user.accessToken)
    if (this.$store.state.authModule.user.accessToken) {
      console.log('token is exist and != []', this.$store.state.authModule.user.accessToken)
      axios.defaults.headers.common['Authorization'] = "Bearer " + this.$store.state.authModule.user.accessToken;
    } else {
      console.log('token is NOT exist')
      // axios.defaults.headers.common['Authorization'] = "";
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/login");
    },
  },
  created() {
    // let link1 = document.createElement('link')
    // link1.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css')
    // document.head.appendChild(link1)
    
    // let links2 = document.createElement('script')
    // links2.setAttribute('src', ' href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"')
    // links2.setAttribute('integrity', 'sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3')
    // links2.setAttribute('crossorigin', 'anonymous')
    // links2.setAttribute('rel', 'stylesheet')

    // document.head.appendChild(links2)

    // let link2 = document.createElement('script')
    // link2.setAttribute('src', 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js')
    // link2.setAttribute('integrity', 'sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB')
    // link2.setAttribute('crossorigin', 'anonymous')
    // document.head.appendChild(link2)

    // let link2 = document.createElement('script')
    // link2.setAttribute('src', 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js')
    // document.head.appendChild(link2)

    // let b1 = document.createElement('link')
    // // b1.setAttribute('rel', 'stylesheet')
    // b1.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js')
    // b1.setAttribute('integrity', 'sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13')
    // b1.setAttribute('crossorigin', 'anonymous')
    // document.head.appendChild(b1)

    // let b1 = document.createElement('link')
    // b1.setAttribute('rel', 'stylesheet')
    // b1.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css')
    // b1.setAttribute('integrity', 'sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn')
    // b1.setAttribute('crossorigin', 'anonymous')
    // document.head.appendChild(b1)


    // let recaptchaScript2 = document.createElement('script')
    // recaptchaScript2.setAttribute('src', 'js/jquery-3.4.1.min.js')
    // document.head.appendChild(recaptchaScript2)

    // let recaptchaScript = document.createElement('script')
    // recaptchaScript.setAttribute('src', 'js/popper.min.js')
    // document.head.appendChild(recaptchaScript)
    // let recaptchaScript1 = document.createElement('script')
    // recaptchaScript1.setAttribute('src', 'js/bootstrap.min.js')
    // document.head.appendChild(recaptchaScript1)
  },
};
</script>
