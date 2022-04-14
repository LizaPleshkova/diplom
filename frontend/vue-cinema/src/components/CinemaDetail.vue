<template>
  <div class="card mx-auto left-ads-display col-lg-12">
    <div class="row">
      <div class="site-section">
        <div class="container-fluid mx-auto">
          <div class="row">
            <div class="col-md-5 mx-2 my-4">
              <div class="border text-center">
                <img
                  v-bind:src="currentCinema?.image"
                  alt="Image"
                  class="img-fluid p-5"
                />
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
              <br />
            </div>
          </div>
        </div>
        <hr />
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <h2 class="text-black">Киносеансы</h2>
              <br />
              <div v-if="cinemaSessions">
                <div class="row justify-content-around row-cols-3 row-cols-md-2">
                  <div
                    class="card border-danger col-md-3 m-2 p-2"
                    v-for="movie_s in cinemaSessions"
                    :key="movie_s.id"
                  >
                      <div class="card-header text-center"><h3>{{ movie_s.movie?.name }}</h3></div>
                      <img
                        class="card-img-top"
                        v-bind:src="movie_s.movie?.image"
                        alt="movie name"
                      />
                      <hr/>
                      <div class="card-body text-center">
                      <div v-for="(genre, ind) in movie_s.movie?.genres"
                          :key="ind">{{ genre}} </div>
                        <hr/>
                         <div v-for="(studio, ind) in movie_s.movie?.studios"
                          :key="ind">{{ studio}} </div>
                        <hr/>
                        <router-link
                          :to="{
                            name: 'movie-session',
                            params: { movieSessionId: movie_s.id },
                          }"
                          class="btn btn-outline-dark"
                        >
                          more details
                        </router-link>
                        <p></p>
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
  name: "cinema-detail",
  computed: mapGetters(["currentCinema", "cinemaSessions", "movieSession"]),
  methods: mapActions(["getCinema"]),
  // mounted() {
  //   this.getCinema(this.$route.params.cinemaId);
  // },
  created() {
    this.getCinema(this.$route.params.cinemaId);
  },
};
</script>
