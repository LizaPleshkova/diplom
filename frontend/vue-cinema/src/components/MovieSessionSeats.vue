<template>
  <div class="justify-content-center m-1 col-sm-6">
    <div class="card col-sm-6 m-1 text-center">
      <div class="card-body bg-danger text-white">
        <p class="card-text">{{ movieSession.movie.name }}</p>
        <span
          >Cinema {{ movieSession.hall.cinema.name }} -
          {{ movieSession.hall.name }}</span
        ><br />
        <span>{{ movieSession.datetime_session }}</span>
      </div>
    </div>

    <div class="row justify-content-center m-1">
      <div class="col-sm-6">
        <div class="site-section">
          <div class="container">
            <div class="row m-1">
              <div class="card text-center">
                <div class="card-header">
                  <h3>Экран</h3>
                </div>
                <div class="card-body">
                  <div
                    class="btn-group"
                    role="group"
                    aria-label="Basic checkbox toggle button group"
                  >

                    <div class="container">
                    <p>{{bookedSeats}}</p>
                      <table class="flex-fill container-fluid bg-">

                        <tbody>
                          <tr v-for="row in allSeats" :key="1">
                            <td v-for="seat in row" :key="seat.id">
                            <div
                                  class="btn-group-toggle"
                                  data-toggle="buttons"
                                >                                
                                  <label class="btn btn-outline-primary" :class="{'disabled': seat.isBooked }" >
                                    <input type="checkbox"  :value="seat.id" v-model="selectedSeats"/> {{ seat.number_place }}
                                  </label>
                               </div>
                            </td>
                          </tr>
                        </tbody>
                        <p>selected seats : {{ selectedSeats }}</p>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row d-flex justify-content-center">
                <button type="submit" @click="bookSeats" class="btn btn-outline-dark m-1">
                  забронировать
                </button>
                <p v-if="newBookedSeats">
                Вы забронировали {{ newBookedSeats }}
                </p>
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
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
// import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min.js'

export default {
  name: "movie-session",
  data() {
    return {
      selectedSeats: [],
    //   newBookedSeats:[],
    };
  },
  computed: mapGetters(["allSeats", "movieSession", "bookedSeats", "newBookSeats"]),
  methods: {
   bookSeats() {

      this.$store.dispatch('BookedSeats', this.selectedSeats);
      this.allSeats = this.$store.dispatch("getSeats",this.movieSession.id);
      console.log(this.allSeats);
   },
     getSeats(){
        this.$store.dispatch("getSeats", this.$route.params.movieSessionId);

  },
  },
  mounted() {
    //inti tooltip
    Array.from(
      document.querySelectorAll('button[data-bs-toggle="tooltip"]')
    ).forEach((tooltipNode) => new Tooltip(tooltipNode));
  },
  beforeMount() {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    this.$store.dispatch("getSeats", this.$route.params.movieSessionId);
  }
};
</script>
