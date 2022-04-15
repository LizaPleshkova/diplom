<template>
  <div class="container-fluid">
    <h3 class="sear-head editContent">Последние добавленные</h3>
    <div class="container">
      <div class="row">
        <div class="card" v-for="movie in latestMovies" :key="movie.id">
          <img :src="movie.image" class="p-3 card-img-top" alt="latest_movie" />
          <div class="card-body">
            <h5 class="card-title text-center">
              {{ movie.name }}
            </h5>
            <div class="card-text text-center">
              <p v-for="(genre, ind) in movie.genres" :key="ind">
                <span>{{ genre.name }} </span>
              </p>
              <router-link
                :to="{ name: 'movie-detail', params: { movieId: movie.id } }"
                class="btn btn-outline-success btn-sm"
                >Read more
              </router-link>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</template>

<script>
import Movie from "./Movie.vue";

export default {
  name: "MovieList",
  components: {
    Movie,
  },
  props: ["movies"],
};
</script>
