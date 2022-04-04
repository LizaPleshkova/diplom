<template lang="">
  <header class="p-3 bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-between">
        <ul
          class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-between mb-md-0"
        >
          <li>
            <router-link to="/" class="nav-link  text-white">
              Home
            </router-link>
          </li>
          <li>
            <router-link to="/cinema" class="nav-link text-white">
              Cinemas
            </router-link>
          </li>
          <li>
            <router-link to="/movie" class="nav-link text-white">
              Movies now
            </router-link>
          </li>
          <li>
            <router-link to="/" class="nav-link px-2 text-white">
              About
            </router-link>
          </li>
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
          <input
            type="search"
            class="form-control form-control-dark"
            placeholder="Search..."
            aria-label="Search"
          />
        </form>

        <div class="text-end ">
         <router-link to="/login">
                      <button type="button" class="m-2 btn btn-outline-light me-2">
            Login
          </button>
            </router-link>
          <router-link to="/register" >
          <button type="button" class="m-2 btn btn-warning ">Sign-up</button>
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {};
</script>
<style lang=""></style>
