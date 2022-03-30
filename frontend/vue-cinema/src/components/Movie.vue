<template>
    <div class="card">
    <img v-bind:src="movie.image" alt="" class="card-img-top">
        <div class="card-body text-center">
            <h5 class="card-title ">{{ movie.name }}</h5>
            <p class="card-text" v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}</p>
            <a href="" class="btn btn-outline-success btn-sm">Read More</a>
        </div>
    </div>
                    
</template>

<script>
export default {
  name: 'Movie',
  props:{
      movie:{
          type:Object,
          default:()=>{}
      }
  }
}
</script>