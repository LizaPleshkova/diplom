<template>
  <div>
    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        кинотеатры
      </div>

      <div class="card-body text-dark">
        <div v-for="cinema in f_cinemas" :key="cinema.id">
          <label class="check">
            {{ cinema.name }}, {{cinema.address}}
            <input
              type="checkbox"
              name="is_name"
              :id="cinema.id"
              :value="cinema.id"
              v-model="selectedCinema"
            />
            <span class="checkmark" :for="cinema.id"></span>
          </label>
        </div>
      </div>
    </div>

    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        жанры
      </div>
      <div class="card-body text-dark">
        <div v-for="genre in f_genres" :key="genre.id">
          <label class="check">
            {{ genre.name }}
            <input
              type="checkbox"
              name="is_name"
              :id="genre.id"
              :value="genre.id"
              v-model="selectedGenres"
            />
            <span class="checkmark" for="genre.id"></span>
          </label>
        </div>
      </div>
    </div>

    <div class="card border-dark mb-2">
      <div class="card-header border-dark bg-transparent text-dark text-center">
        даты
      </div>
      <div class="card-body text-dark">
        <div v-for="(date, ind) in f_dates" :key="ind">
          <label class="check">
            {{ date }}
            <input
              type="checkbox"
              name="is_name"
              :id="ind"
              :value="date"
              v-model="selectedDates"
            />
            <span class="checkmark" :for="ind"></span>
          </label>
        </div>
      </div>
    </div>

    <div class="d-grid">
      <button
        type="submit"
        value="submit"
        v-on:click="getFilterMovies"
        class="btn btn-outline-dark btn-sm-6 btn-block"
      >
        find
      </button>
    </div>
  </div>
</template>

<script>
import FilterService from "@/services/FilterService.js";
import { mapGetters } from "vuex";

export default {
  name: "Filters",

  data() {
    return {
      f_cinemas: [],
      f_genres: [],
      f_dates: [],

      selectedCinema: [],
      selectedGenres: [],
      selectedDates: [],
    };
  },
  computed: mapGetters(["allMovies"]),
  methods: {
    getFilterMovies: async function () {
      var filters = {
        selectedCinema: this.selectedCinema,
        selectedGenres: this.selectedGenres,
        selectedDates: this.selectedDates,
      };
      console.log("filters", filters);
      this.$store.dispatch("getFilterMovies", filters);
    },
  },

  created() {
    FilterService.getFilters().then((filters) => {
      this.f_cinemas = filters["cinemas"];
      this.f_dates = filters["dates"];
      this.f_genres = filters["genres"];
    });
  },
};
</script>

<style>
/* The radio */
.radio {
  display: block;
  position: relative;
  padding-left: 30px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 10px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default radio button */
.radio input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

/* Create a custom radio button */
.checkround {
  position: absolute;
  top: 6px;
  left: 0;
  height: 20px;
  width: 20px;
  background-color: #fff;
  border-color: #13c931;
  border-style: solid;
  border-width: 2px;
  border-radius: 50%;
}

/* When the radio button is checked, add a blue background */
.radio input:checked ~ .checkround {
  background-color: #fff;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkround:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the indicator (dot/circle) when checked */
.radio input:checked ~ .checkround:after {
  display: block;
}

/* Style the indicator (dot/circle) */
.radio .checkround:after {
  left: 2px;
  top: 2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #09b425;
}

/* The check */
.check {
/* justify-content-around; */
  display: block;
  position: relative;
  padding-left: 25px;
  margin-bottom: 12px;
  padding-right: 15px;
  cursor: pointer;
  font-size: 15px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.check input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 3px;
  left: 0;
  height: 18px;
  width: 18px;
  background-color: #fff;
  border-color: #08c904;
  border-style: solid;
  border-width: 2px;
}

/* When the checkbox is checked, add a blue background */
.check input:checked ~ .checkmark {
  background-color: #fff;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.check input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.check .checkmark:after {
  left: 5px;
  top: 1px;
  width: 5px;
  height: 10px;
  border: solid;
  border-color: #f8204f;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

.cust-btn {
  margin-bottom: 10px;
  background-color: #f8204f;
  border-width: 2px;
  border-color: #f8204f;
  color: #fff;
}
.cust-btn:hover {
  border-color: #f8204f;
  background-color: #fff;
  color: #f8204f;
  border-radius: 20px;
  transform-style: 2s;
}
</style>
