<template>
  <div id="#app">
    <Header />
    <div id="page" class="page">
      <!-- mian-content -->
      <div
        class="main-banner bg bg1"
        id="home"
        style="
          background-color: rgba(0, 0, 0, 0);
          margin-top: 0px;
          background-image: url('/static/try4.jpg');
        "
      >
        <div class="banner-info">
          <p class="editContent">for booking</p>
          <h3 class="mb-4 editContent">Cinema</h3>
        </div>
      </div>
    </div>
    <ol class="breadcrumb editContent">
      <li class="breadcrumb-item">
        <a href="#" class="editContent">Home</a>
      </li>
    </ol>
    <section
      class="ab-info-main py-md-5 py-4 editContent"
      style="padding-left: 3rem; padding-right: 3rem"
    >
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
      axios.defaults.headers.common['Authorization'] = "Bearer " + this.$store.state.authModule.user.accessToken;
    } else {
      axios.defaults.headers.common['Authorization'] = "";
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/login");
    },
  },
};
</script>
