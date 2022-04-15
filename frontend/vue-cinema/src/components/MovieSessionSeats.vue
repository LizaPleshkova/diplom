<template>
  <div class="container col-sm-6">
    <div class="row">

      <div class="col-sm-12 m-1 text-center">
        <div class="card-body bg-danger text-white">
          <p class="card-text"><h4>{{ movieSession.movie?.name }}</h4></p>
          <span
            >Cinema {{ movieSession.hall?.cinema.name }} -
            {{ movieSession.hall.name }}</span
          ><br />
          <span>{{ movieSession.datetime_session }}</span>
        </div>
      </div>
      <div class="col-sm-12 m-1 text-center " v-if='errorMessage'>
       <div class="alert alert-warning" role="alert">
        {{ errorMessage }}
      </div>
      </div>
      <div class="col-sm-12 m-1 text-center " v-if='newBookSeats.length != 0'>
        <div class="alert alert-success" role="alert">
         <h6> The booking was successful! You can view all your booked tickets in profile.</h6>
      </div>
      </div>
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
import { nextTick } from 'vue'
import axios from "axios";


const headers = { 
    "Content-type": "application/json",
    'Authorization': "Bearer " + localStorage.getItem('token')
  };

export default {
  name: "movie-session",
  data() {
    return {
      selectedSeats: [],
      allSeats:[],
      movieSession:[],
      newBookSeats:[],
      allBookedSeats:[],

      errorMessage:null
    };
  },
  methods: {
   bookSeats() {
     this.newBookSeats=[];
      axios.post( 
        `http://localhost:8000/api/movie-session/${this.movieSession.id}/booking/ `, this.selectedSeats,
        {headers})
    .then(response => {
      this.newBookSeats = response.data;
      console.log(this.newBookSeats)
 
      var ids_booked_seats=[];
      this.newBookSeats.forEach(el => ids_booked_seats.push(el['seat']));

      for (var row in this.allSeats) {
          var seats = this.allSeats[row];

          for (var k_seat in seats) {
            if (ids_booked_seats.indexOf(seats[k_seat].id) != -1) {
              seats[k_seat]["isBooked"] = true;
              console.log('true',seats[k_seat])
            }
          }
      }
    })
    .catch(error => {
      this.errorMessage = error.message;
      console.error("There was an error!", error);
    });
    this.$data.selectedSeats=[];
    this.seleсtedSeats=[];
    },
    getSeats(pk){
      axios.get( `http://localhost:8000/api/movie-session/${pk}/seats/ `,{
      "Content-type": "application/json",
      'Authorization': "Bearer " + localStorage.getItem('token')})
      .then((response )=> {
      console.log( response.data['seat_layout'], response.data['movie_session'] )
        this.seleсtedSeats=[];
        this.allSeats = response.data['seat_layout']
        this.movieSession = response.data['movie_session']
      })
      .catch(error => {
      this.errorMessage = error.message;
      console.error("There was an error!", error);
      });
    },
  },
  mounted() {
    //inti tooltip
    Array.from(
      document.querySelectorAll('button[data-bs-toggle="tooltip"]')
    ).forEach((tooltipNode) => new Tooltip(tooltipNode));
  },
  async created(){
    this.getSeats(this.$route.params.movieSessionId);
    console.log(this.allSeats, this.movieSession)

  //  var data =  await MovieSessionService.getSeats(this.$route.params.movieSessionId).then((data) => {
  //     console.log(data);
  //     return data;
  //   });
  //       this.allSeats = data['seat_layout']
  //       this.movieSession = data['movie_session']
  //       console.log(this.allSeats, this.movieSession)
  },
};
</script>
