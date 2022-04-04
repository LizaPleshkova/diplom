<template>
  <div class="side-bar col-sm-3">
    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Кинотеатры
      </div>
      <div class="card-body text-dark"></div>
    </div>

    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Даты
      </div>
      <div class="card-text text-center m-1"></div>
    </div>

    <div class="card border-dark mb-3">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        Жанры
      </div>
      <div class="card-text text-center"></div>
    </div>
  </div>

  <div class=" col-sm-9">
  <div class="row row-cols-3 row-cols-md-3">

      <MovieList :movies="allMovies" />
    </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieList from "@/components/MovieList";

export default {
  name: "Main",
  components: {
    MovieList,
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
