<template>
  <div class="container col-sm-6">
    <div class="row">
      <div class="col-sm-12 m-1 text-center">
        <div class="card-body bg-danger text-white">
          <p class="card-text"><h4>{{ movieSession.movie?.name }}</h4></p>
          <span
            >Cinema {{ movieSession.hall.cinema.name }} -
            {{ movieSession.hall.name }}</span
          ><br />
          <span>{{ movieSession.datetime_session }}</span>
        </div>
      </div>
      {{bookedSeats}}
      <div class="col-sm-12">
              <div class="card text-center">
                <div class="card-header">
                  <h3>screen</h3>
                </div>
                <div class="card-body">
                  <div
                    class="btn-group"
                    role="group"
                    aria-label="Basic checkbox toggle button group"
                  >
                    <div class="container">
                      <table class="flex-fill container-fluid">
                        <tbody>
                        
                          <tr v-for="(row, ind) in allSeats" :key="ind">
                            <td v-for="seat in row" :key="seat.id"><div class="btn-group-toggle" data-toggle="buttons" >
                                <label
                                  class="btn btn-outline-secondary m-1"
                                  :class="{ disabled: seat.isBooked }"
                                  :title="'Sector-'+ seat.sector + ', price- '+ seat.price"
                                >
                                  <input
                                    type="checkbox"
                                    :value="seat.id"
                                    v-model="selectedSeats"
                                  />
                                  {{ seat.number_place }}
                                </label>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
                <div class="card-footer">
                  <button
                  type="submit"
                  @click="bookSeats"
                  class="btn btn-outline-dark m-1"
                 >
                  book
                 </button>
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
import MovieSessionService from "@/services/MovieSessionService.js";
// import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min.js'
import { nextTick } from 'vue'

export default {
  name: "movie-session",
  data() {
    return {
      selectedSeats: [],
      allSeats:[],
      movieSession:[],
      newBookSeats:[],
      bookedSeats:[]
    };
  },
  methods: {
   async bookSeats() {
      
      MovieSessionService.bookSeats(this.selectedSeats, this.movieSession.id)
      .then((data)=>{
            this.newBookSeats = data;
            console.log(this.newBookSeats)
        });
      console.log(this.allSeats);
      this.getSeats(this.movieSession.id);

      // var data =  await MovieSessionService.getSeats(this.$route.params.movieSessionId).then((data) => {
      // console.log(data);
      console.log('after get_seats',this.allSeats)
      //     nextTick(() => {
      //   console.log(this.allSeats)
      //    console.log(this.$refs.allSeats.innerText)
      // })
       
        // console.log(this.allSeats, this.movieSession)

    },
    getSeats(pk){
        // MovieSession.getSeats
        var dat =   MovieSessionService.getSeats(this.$route.params.movieSessionId).then((data) => {
      // console.log(data);
      return data;
    });
    console.log('data', dat)

        this.allSeats = dat['seat_layout']
        this.movieSession = dat['movie_session']
    },
    // getSeatss() {
    //   this.$store.dispatch("getSeats", this.$route.params.movieSessionId);
    // },
  },
  mounted() {
    //inti tooltip
    Array.from(
      document.querySelectorAll('button[data-bs-toggle="tooltip"]')
    ).forEach((tooltipNode) => new Tooltip(tooltipNode));
  },
  async created(){
   var data =  await MovieSessionService.getSeats(this.$route.params.movieSessionId).then((data) => {
      console.log(data);
      return data;
    });
        this.allSeats = data['seat_layout']
        this.movieSession = data['movie_session']
        console.log(this.allSeats, this.movieSession)
  },
};
</script>
