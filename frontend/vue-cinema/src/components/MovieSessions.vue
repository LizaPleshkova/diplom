<template>
  <div class="row">
    <div class="col-md-12">
      <h2 class="text-black">Киносеансы</h2>
      <br />
      <div v-if="sessions != []">
        <div class="row row-cols-3 row-cols-md-2">
          <div
            class="card col-md-3 m-4"
            v-for="movie_s in sessions"
            :key="movie_s.id"
          >
            <div class="card border text-center border-danger m-3">
              <div class="card-header bg-danger text-white">
                {{ movie_s.hall.name }} зал
              </div>
              <div class="card-body text-center">
                <router-link
                  :to="{
                    name: 'movie-session',
                    params: { movieSessionId: movie_s.id },
                  }"
                  class="btn btn-outline-dark"
                >
                  {{ movie_s.datetime_session.time }}
                </router-link>
                <p>
                  {{ movie_s.datetime_session.date }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Киносеансов на данный фильм пока что нет</p>
        <p>Попробуйте выбрать другой фильм</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "MovieSessions",
  props: ["sessions"],
  created() {
    console.log("from MS", this.sessions);
  },
  //   computed: mapGetters(["currentMovie", "movieSessions"]),
  //   methods: mapActions(["getMovie"]),
  //   created() {
  //     console.log("from MD", this.$route.params.movieId);
  //     this.getMovie(this.$route.params.movieId);
  //     console.log(this.currentMovie, this.movieSessions);
  //   },
};
</script>
