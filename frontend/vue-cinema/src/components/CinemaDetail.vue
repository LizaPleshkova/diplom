<template>
  <div class="card mx-auto left-ads-display col-lg-12">
    <div class="row">
      <div class="site-section">
        <div class="container-fluid mx-auto">
          <div class="row">
            <div class="col-md-5 mx-2 my-4">
              <div class="border text-center">
                <img v-bind:src="currentCinema?.image" alt="Image" class="img-fluid p-5" />
              </div>
            </div>

            <div class="col-md-5 mx-4 my-4">
              <p class="small font-weight-bold my-2">cinema</p>
              <h3 class="mb-3">
                {{ currentCinema?.name }}
              </h3>
              <p>
                <strong>Address: </strong>{{ currentCinema?.address }}<br />
                <strong>Phone number: </strong>{{ currentCinema?.phone_number
                }}<br />
              </p>
              <hr />
              <p>
                {{ currentCinema?.description }}
              </p>
              <br />
            </div>
          </div>
        </div>
        <hr />
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <h2 class="text-black text-center">Киносеансы</h2>
              <br />
              <div v-if="cinemaSessions">
                <div class="row row-cols-2 row-cols-md-4 justify-content-around">
                  <div class="card m-2 p-2" v-for="movie_s in cinemaSessions" :key="movie_s.id">
                    <img v-bind:src="movie_s.movie.image" alt="" class="card-img-top" />
                    <div class="card-body text-center">
                      <h1 class="card-title">{{ movie_s.movie.name }}</h1>
                      <p class="card-text" v-for="genre in movie_s.movie.genres" :key="genre.id">
                        {{ genre }} </p>

                      <router-link :to="{ name: 'movie-detail', params: { movieId: movie_s.movie.id } }"
                        class="btn btn-outline-success btn-sm">Read more
                      </router-link>
                    </div>
                  </div>

                </div>
              </div>
              <div v-else>
                <p>Киносеансов в кинотеатре {{ currentCinema?.name }} на текузий момент нет</p>
                <p>Попробуйте выбрать другой кинотеатр или перезагрузить страницу</p>
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
  name: "cinema-detail",
  computed: mapGetters(["currentCinema", "cinemaSessions", "movieSession"]),
  methods: mapActions(["getCinema"]),
  created() {
    this.getCinema(this.$route.params.cinemaId);
  },
};
</script>
