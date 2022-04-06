<template lang="">
  <nav
    class="navbar navbar-expand-lg navbar-dark bg-dark"
    style="margin: 24px 0"
  >
    <router-link to="/" class="navbar-brand"
      >CityCinema</router-link
    >

    <div class="collapse navbar-collapse" id="navb">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/movie" class="nav-link"
            >Movies</router-link
          >
        </li>
        <li class="nav-item">
          <router-link to="/cinema" class="nav-link"
            >Cinema</router-link
          >
        </li>
        <li class="nav-item">
          <router-link to="/" class="nav-link"
            >About</router-link
          >
        </li>
      </ul>
    </div>

    <form class="form-inline my-4 my-lg-0 m-3">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" />
      <button class="btn btn-success my-2 my-sm-0" type="button">Search</button>
    </form>
    <div
      class="dropdown m-3"
      v-if="$store.state.authModule.user.isAuthenticated"
    >
      <button
        class="btn btn-secondary dropdown-toggle"
        type="button"
        id="dropdownMenuButton"
        data-toggle="dropdown"
        aria-expanded="false"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-person-circle"
          viewBox="0 0 16 16"
        >
          <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"></path>
          <path
            fill-rule="evenodd"
            d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
          ></path>
        </svg>
      </button>
      <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <router-link to="/profile" class="dropdown-item">Profile </router-link>
        <router-link to="/logout" class="dropdown-item"> LogOut</router-link>
      </div>
    </div>

    <div v-else>
      <router-link to="/login">
        <button type="button" class="btn btn-outline-warning m-3">
          Login
        </button></router-link
      >
      <router-link to="/sign-up">
        <button type="button" class="btn btn-outline-warning">
          Sign Up
        </button></router-link
      >
    </div>
  </nav>
</template>

<script>
export default {};
</script>
<style lang=""></style>
