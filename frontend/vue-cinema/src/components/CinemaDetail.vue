<template>
  <div class="card">
    <h1>cinema</h1>
    <div class="card">
      <div class="card-body text-center">
        <img v-bind:src="currentCinema.image" alt="" class="card-img-top" />
        <h5 class="card-title">{{ currentCinema.name }}</h5>
        <div class="card-text">
          <p>{{ currentCinema.address }}</p>
          <p>{{ currentCinema.phone_number }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex' 


export default {
  name: "cinema-detail",
  computed: mapGetters(["currentCinema"]),
  methods: mapActions(["getCinema"]),
  // mounted() {
  //   this.getCinema(this.$route.params.cinemaId);
  // },
  created(){
    this.getCinema(this.$route.params.cinemaId);

  }
};
</script>
