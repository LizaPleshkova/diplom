<template>
  <div class="col mb-4">
    <div class="card">
      <img v-bind:src="movie.image" alt="" class="card-img-top"/>
      <div class="card-body text-center p-2 m-1">
        <h3 class="card-title">{{ movie.name }}</h3>
        <p class="card-text m-1" v-for="(genre, ind ) in movie.genres" :key="ind">
          {{ genre }} </p>
          
         <router-link :to="{ name: 'movie-detail', params: { movieId: movie.id } }"
        class="btn btn-outline-success btn-sm m-2"
        >Подробнее
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
