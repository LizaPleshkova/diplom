<template>
  <div class="col mb-4">
    <div class="card">
      <img v-bind:src="movie.image" alt="" class="card-img-top"/>
      <div class="card-body text-center">
        <h1 class="card-title">{{ movie.name }}</h1>
        <p class="card-text" v-for="genre in movie.genres" :key="genre.id">
          {{ genre.name }} </p>
          
         <router-link :to="{ name: 'movie-detail', params: { movieId: movie.id } }"
        class="btn btn-outline-success btn-sm"
        >Read more
      </router-link>
      </div>
    </div>
    </div>
</template>
<script>

export default {
  name: "Movie",
    // computed:mapGetters(['allCinema']),
  props:[ 'movie'],
  created(){
    console.log('from M', this.movie)
  }
//   mounted(){
//         console.log(this.movies);

//   }
};
</script>
