<template>
  <div>
    <div class="display-4 font-weight-bold text-center">{{ currentMovie?.name }}</div>
    <div class="card mx-auto left-ads-display col-lg-12">

      <div class="row">
        <div class="site-section">
          <div class="container-fluid mx-auto">
            <div class="row">
              <div class="col-md-12 mx-2 my-4">
                <div>
                  <img v-bind:src="currentMovie.image" alt="Image" style="width: 25rem;" class="img-responsive lefting mt-6 px-2"  />
                 <!-- <br/> -->
                  <p class="display-6 font-weight-normal mt-1 p-2  mt-2"><strong>Дата выхода: </strong> {{ currentMovie.release_date
                  }}</p>
                  <p class=" display-6 font-weight-normal">
                    <strong>Страны: </strong>{{ currentMovie.countries }}
                  </p>
                  <p class=" display-6 font-weight-normal"><strong>Жанра: </strong> {{ currentMovie.genres }} </p>

                  <p class=" display-6 font-weight-normal"><strong>Студии: </strong> {{ currentMovie.studios }} </p>
                  <p class=" display-6 font-weight-normal"><strong>Возрастная категория: </strong> {{
                      currentMovie.category
                  }}+</p>
                  <p class=" display-6 font-weight-normal"><strong>Длительность: </strong> {{ currentMovie.duration }}
                  </p>
                  <hr />
                  <p>{{ currentMovie.description }}</p>
                </div>
              </div>
            </div>
          </div>
          <hr />

          <div class="container">
            <MovieSessions :sessions="movieSessions" />
          </div>

        </div>
      </div>
      <div>
        <div class="row">
          <CommentsMovie />
        </div>
      </div>


    </div>
  </div>

</template>

<script>
import { mapGetters, mapActions } from "vuex";
import CommentsMovie from "./CommentsMovie.vue";
import MovieSessions from "./MovieSessions.vue";

export default {
  name: "movie-detail",
  components: {
    CommentsMovie, MovieSessions
  },
  props: ['sessions'],
  computed: mapGetters(["currentMovie", "movieSessions"]),
  methods: mapActions(["getMovie"]),
  created() {

    this.getMovie(this.$route.params.movieId);
    console.log('that', this.currentMovie, this.movieSessions, this.isAuthenticated);
  },
};
</script>
<style>
.lefting {
  float: left;
  margin: 10px 10px 10px 10px;
}
</style>
