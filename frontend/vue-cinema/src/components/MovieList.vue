<template>
        <Movie v-for="movie in movies" v-bind:key="movie.id" :movie="movie" />
      
</template>

<script>
import Movie from "./Movie.vue";

export default {
  name: "MovieList",
  components: {
    Movie,
  },
  props: ["movies"]
};
</script>
