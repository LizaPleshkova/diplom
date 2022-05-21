<template>
  <div class="row">
    <div class="side-bar col-sm-2 navbar-nav mr-auto">
      <Filters />
    </div>

    <div class="col-sm-10">
      <div class="row row-cols-3 row-cols-md-3">
        <MovieList :movies="allMovies" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieList from "@/components/MovieList";
import Filters from "@/components/Filter.vue";

export default {
  name: "Main",
  components: {
    MovieList,
    Filters,
  },
  computed: mapGetters(["allMovies"]),
  methods: mapActions(["getMovies"]),
  mounted() {
    this.getMovies();
  },
};
</script>

<style lang="scss" scoped>
header {
  background-color: #0c0c0c;
  .container {
    margin-top: 0;
    display: flex;
    align-items: baseline;
  }
  padding: 20px 0;
  a {
    text-decoration: none;
    font-weight: 700;
    color: #ffffff;
    font-size: 25px;
  }
  .logo {
    color: #eb5804;
    font-size: 30px;
  }
  .links {
    margin-left: 75px;
    display: flex;
    flex-grow: 1;
  }
  button {
    margin-left: auto;
  }
}
</style>
