<template>
  <div class="container-fluid"> 
    <div class='row'>
        <div class="col-sm-9">
       
          <Cinema
            v-for="cinema in allCinemas"
            v-bind:key="cinema.id"
            :cinema="cinema"
          />
        </div>
        <div class="col-sm-3">
         <h3 class="text-center">Скоро в прокате</h3><hr/>
          <MovieSoon v-for="movie in movieSoon"
            v-bind:key="movie.id"
            :movie="movie"
            />
        </div>
        </div>
  </div>
</template>

<script>
import Cinema from "./Cinema.vue";
import MovieSoon from "./MovieSoon.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CinemaList",
  components: {
    Cinema, MovieSoon
  },
  computed: mapGetters(["allCinemas", "movieSoon"]),
  methods: mapActions(["getCinemas", "getMoviesSoon"]),
  mounted() {
    this.getCinemas();
    this.getMoviesSoon();
    console.log(this.allCinemas);
  },
};
</script>
