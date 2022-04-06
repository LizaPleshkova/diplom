<template>
  <div class="side-bar col-sm-3">
    <Filters />
  </div>

  <div class="col-sm-9">
    <div class="row row-cols-3 row-cols-md-3">
      <MovieList :movies="allMovies" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import MovieList from "@/components/MovieList";
import Filters from "@/components/Filter.vue";

export default {
  name: "Main",
  //   data(){
  //     return{
  //       f_cinemas:[],
  //       f_genres:[],
  //       f_dates:[]
  //     }
  // },
  //  created(){
  //       FilterService.getFilters().then((cinemas, genres, dates) => {
  //           this.f_cinemas = cinemas;
  //           this.f_dates = dates;
  //           this.f_genres = genres;

  //           console.log(this.f_cinemas);
  //           console.log(this.f_genres);
  //           console.log(this.f_dates);
  //       });
  // },
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
