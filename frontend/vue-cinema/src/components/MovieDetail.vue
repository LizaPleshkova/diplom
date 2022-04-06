<template>
  <div class="card mx-auto left-ads-display col-lg-12">
    <div class="row">
      <div class="site-section">
        <div class="container-fluid mx-auto">
          <div class="row">
            <div class="col-md-5 mx-2 my-4">
              <div class="border text-center">
                <img
                  v-bind:src="currentMovie.image"
                  alt="Image"
                  class="img-fluid p-5"
                />
              </div>
            </div>

            <div class="col-md-5 mx-4 my-4">
              <h2 class="text-black">{{ currentMovie.name }}</h2>
              <br />
              <p>{{ currentMovie.description }}</p>
              <hr />

              <h4 class="text-black">Год:</h4>
              <p>{{ currentMovie.release_date }}</p>
              <h4 class="text-black">Страна:</h4>
              <p v-for="country in currentMovie.countries" :key="country.id">
                {{ country.name }}
              </p>
              <h4 class="text-black">Жанры:</h4>
              <p v-for="genre in currentMovie.genres" :key="genre.id">
                {{ genre.name }}
              </p>
              <h4 class="text-black">Студия:</h4>
              <p v-for="st in currentMovie.studios" :key="st.id">
                {{ st.name }}
              </p>
              <h4 class="text-black">Возрастная категория:</h4>
              <p>{{ currentMovie.category }}+</p>
              <h4 class="text-black">Длительность:</h4>
              <p>{{ currentMovie.duration }}</p>
            </div>
          </div>
        </div>
        <hr />

        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <h2 class="text-black">Киносеансы</h2>
              <br />

              <div v-if="movieSession != null">
                <div class="row row-cols-3 row-cols-md-2">
                  <div
                    class="card col-md-3 m-4"
                    v-for="movie_s in movieSession"
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
                            {{ movie_s.datetime_session }}
                          </router-link> 
                          <p>
                            {{ movie_s.datetime_session }}
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
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "movie-detail",
  computed: mapGetters(["currentMovie", "movieSession"]),
  methods: mapActions(["getMovie"]),
  created() {
    console.log("from MD", this.$route.params.movieId);
    this.getMovie(this.$route.params.movieId);
    console.log(this.currentMovie, this.movieSession);
  },
};
</script>
