<template>
      <div class="card p-3">
          <img :src="movie.image" class=" card-img-top" alt="latest_movie" />
          <div class="card-body">
            <h6 class="card-title text-center">
              {{ movie.name }}
            </h6>
            <div class="card-text text-center">
              <div v-for="genre in movie.genres" :key="1" class='small'>
                <span>{{ genre }} </span>
              </div>
              <p></p>
              <router-link
                :to="{ name: 'movie-detail', params: { movieId: movie.id } }"
                class="btn btn-outline-success btn-sm"
                >Read more
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
