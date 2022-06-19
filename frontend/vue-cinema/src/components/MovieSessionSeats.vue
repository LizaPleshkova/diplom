<template>
  <div class="container col-sm-6">
    <div class="row">

      <div class="col-sm-12 m-1 text-center">
        <div class="card-body bg-danger text-white">
          <p class="card-text">
          <h4>{{ movieSession.movie?.name }}</h4>
          </p>
          <span>Кинотеатр {{ movieSession.hall?.cinema.name }} -
            зал {{ movieSession.hall.name }}</span><br />
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
          <h6>Бронирование прошло успешно! Все актуальные брони можешь просмотреть в твоем профиле.</h6>
        </div>
      </div>
      <div class="col-sm-12 m-1 text-center " v-if='!isAuthenticated'>
        <div class="alert alert-info m-1 text-center" role="alert" v-if="!isAuthenticated">
          Для того, чтобы заброинровать место необходимо авторизоваться!
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card text-center">
          <div class="card-header">
            <h3>экран</h3>
          </div>

          <div class="card-body">
            <div class="btn-group" role="group" aria-label="Basic checkbox toggle button group">
              <div class="container">
                <table class="flex-fill container-fluid">
                  <tbody>
                    <tr v-for="(row, ind) in allSeats" :key="ind">
                      <button type="button" class="btn btn-outline-primary btn-sm mr-4 p-1" disabled>{{ ind }}
                        ряд</button>
                      <!-- <p class ="m-2"> {{ ind }} ряд       </p> -->
                      <td v-for="seat in row" :key="seat.id">
                        <div class="checkbox-btn-group">

                          <label class="checkbox-btn m-1" :class="{ 'disabled-seat': seat.isBooked }"
                            :title="'Sector-' + seat.sector + ', price- ' + seat.price">
                            <input type="checkbox" :value="seat.id" v-model="selectedSeats" />
                            <span>{{ seat.number_place }}</span>
                            <!-- <span>Checkbox #3</span> -->
                          </label>
                          <!-- <label class="btn btn-outline-secondary m-1" :class="{ disabled: seat.isBooked }"
                            v-on:click="updateTotalPrice(seat)"
                            :title="'Sector-' + seat.sector + ', price- ' + seat.price">
                            <input type="checkbox" :value="seat.id" v-model="selectedSeats" />
                            {{ seat.number_place }}
                          </label> -->
                        </div>
                      </td>

                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

          </div>
          <div class="card-footer">
            <button type="submit" @click="bookSeats" class="btn btn-outline-dark m-1"
              :class="{ 'disabled-button': closeBooking() }">
              забронировать
            </button>
          </div>
        </div>
        <div class="card text-center">
          <div class="card-body">
            <p>всего мест: {{ selectedSeats.length }}, общая сумма: {{ totalPrice }} </p>
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

// let timerId = setInterval(() => alert('tick'), 2000); 

const headers = {
  "Content-type": "application/json",
  'Authorization': "Bearer " + localStorage.getItem('token')
};

export default {
  name: "movie-session",
  data() {
    return {
      selectedSeats: [],
      allSeats: [],
      movieSession: [],
      newBookSeats: [],
      allBookedSeats: [],
      rowNum: 0,
      totalPrice: 0,
      isAuthenticated: this.$store.state.authModule.user.isAuthenticated,
      errorMessage: null
    };
  },
  methods: {
    closeBooking() {
      // к киносеансу добавляю час и если он все еще до now -> до киносенаса осталось больще час и еще можно бронировать
      // return false -> доступ закрыт для броин
      var session_time = new Date(this.movieSession.datetime_session)
      console.log(session_time, typeof (session_time))
      session_time.setMinutes(session_time.getMinutes() + 60)
      session_time = new Date(session_time)
      var now = new Date();
      console.log(now, !this.isAuthenticated, session_time <= now, !this.isAuthenticated || session_time <= now);
      if (!this.isAuthenticated ||
        (session_time.getDate() <= now.getDate() &&
          session_time.getMonth() <= now.getMonth() &&
          session_time.getFullYear() <= now.getFullYear())
      ) {
        if (
          session_time.getHours() <= now.getHours() &&
          session_time.getMinutes() <= now.getMinutes()
        ) {
          console.log(session_time <= now)
          return true
        }
        else {
          console.log(session_time <= now)

          return false
        }

      }
      else{
        return false
      }
    },
    updateTotalPrice(seat) {
      if (seat.id in this.selectedSeats) {
        console.log(this.totalPrice);
        this.totalPrice = this.totalPrice + seat.price;
      }
      this.totalPrice = this.totalPrice - seat.price;

    },
    bookSeats() {
      this.newBookSeats = [];
      axios.post(
        `http://localhost:8000/api/booking/${this.movieSession.id}/movie-session/booking-seats/ `, this.selectedSeats,
        { headers })
        .then(response => {
          this.newBookSeats = response.data;

          // var ids_booked_seats = [];
          // this.newBookSeats.forEach(el => ids_booked_seats.push(el['seat']));

          // for (var row in this.allSeats) {
          //   var seats = this.allSeats[row];

          //   for (var k_seat in seats) {
          //     if (ids_booked_seats.indexOf(seats[k_seat].id) != -1) {
          //       seats[k_seat]["isBooked"] = true;
          //       console.log('true', seats[k_seat])
          //     }
          //   }
          // }
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      this.$data.selectedSeats = [];
      this.seleсtedSeats = [];
    },
    getSeats(pk) {
      axios.get(`http://localhost:8000/api/movie-session/${pk}/seats/ `, {
        "Content-type": "application/json",
        'Authorization': "Bearer " + localStorage.getItem('token')
      })
        .then((response) => {
          console.log('seat layout', response.data['seat_layout'], response.data['movie_session'])
          this.seleсtedSeats = [];
          this.allSeats = response.data['seat_layout']
          this.movieSession = response.data['movie_session']
          this.movieSession.datetime_session = new Date(this.movieSession.datetime_session).toLocaleString();
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
    },
  },
  watch: {
    newBookSeats(newBookedSeats, oldBookSeats) {
      if (newBookedSeats !== oldBookSeats) {
        this.getSeats(this.$route.params.movieSessionId);
      }
    },
  },
  mounted() {
    //inti tooltip
    Array.from(
      document.querySelectorAll('button[data-bs-toggle="tooltip"]')
    ).forEach((tooltipNode) => new Tooltip(tooltipNode));
  },
  async created() {
    this.getSeats(this.$route.params.movieSessionId);
  },
};
</script>

<style>
.disabled-button {
  pointer-events: none;
  cursor: default;
}

.disabled-seat {
  pointer-events: none;
  cursor: default;
  background: #ffffff;
  color: rgb(209, 202, 202);
}

.checkbox-btn {
  display: inline-block;
  margin: 0 5px 0 0;
  user-select: none;
  position: relative;
}

.checkbox-btn input[type=checkbox] {
  z-index: -1;
  opacity: 0;
  display: block;
  width: 0;
  height: 0;
}

.checkbox-btn span {
  display: inline-block;
  cursor: pointer;
  padding: 0px 10px;
  line-height: 30px;
  border: 1px solid #999;
  border-radius: 4px;
  transition: background 0.2s ease;
}

/* Checked */
.checkbox-btn input[type=checkbox]:checked+span {
  /* background: #f63d3078; */
  /* background: rgba(247, 65, 83, 0.226); */
  background: rgba(59, 201, 90, 0.192);
}

/* Focus */
.focused span {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, .25);
}

/* Hover */
.checkbox-btn:hover {
  color: #666;
}

/* Active */
.checkbox-btn input[type=checkbox]:active:not(:disabled)+span {
  background: #d2c5ac;
  color: rgb(89, 78, 78);
}

/* Disabled */
.checkbox-btn input[type=checkbox]:disabled+span {
  background: #efefef;
  color: #666;
  cursor: default;
}

.checkbox-btn input[type=checkbox]:checked:disabled+span {
  background: #f7efdc;
}
</style>