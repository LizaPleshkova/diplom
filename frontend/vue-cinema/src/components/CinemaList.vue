<template>
  <div class="left-ads-display col-lg-9">
    <div class="row" id="gallery">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 mb-4">
            <h1>from cinema list</h1>
            <Cinema
              v-for="cinema in allCinemas"
              v-bind:key="cinema.id"
              :cinema="cinema"
            />
            <!-- query: { id: cinema.id }-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Cinema from "./Cinema.vue";
import {mapGetters, mapActions} from 'vuex' 

export default {
  name: "CinemaList",
  components: {
    Cinema,
  },
  computed:mapGetters(['allCinemas']),
  methods: mapActions(['getCinemas']),
  mounted(){
    this.getCinemas();
    console.log(this.allCinemas);
  }
};
</script>
