<template>
  <div class="left-ads-display col-lg-9">
    <div class="row">
        <section id="gallery">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 mb-4">

                        <Movie v-for="movie in movies" v-bind:key="movie.id" :movie="movie"/>
                    </div>
                </div>
            </div>
        </section>
    </div>
</div>
</template>

<script>
import Movie from "./Movie"

export default {
  name: 'MovieList',
  data() {
    return {
      movies: [],
    };
  },
  components:{
    Movie
  },
  async created(){
    var response = await fetch('http://localhost:8000/api/movie/');
    this.movies = await response.json();console.log(this.movie);
  }
}
</script>