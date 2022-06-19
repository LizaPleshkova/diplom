<template>
      <div class="card m-3">
          <img :src="movie.image" class=" card-img-top" alt="latest_movie" />
          <div class="card-body">
            <h5 class="card-title text-center">
              {{ movie.name }}
            </h5>
            <div class="card-text text-center p-1">
              <div v-for="genre in movie.genres" :key="1" class='small'>
                <span>{{ genre }} </span>
              </div>
              <router-link
                :to="{ name: 'movie-detail', params: { movieId: movie.id } }"
                class="btn btn-outline-success btn-sm m-2"
                >подробнее
              </router-link>
            </div>
          </div>
      </div>

</template>

<script>

export default {
  name: "MovieSoon",
  props: ["movie"],
};
</script>
