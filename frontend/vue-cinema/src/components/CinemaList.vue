<template>
  <div class="left-ads-display col-lg-9">
    <div class="row">
        <section id="gallery">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 mb-4">
                    <Cinema v-for="cinema in cinemas" v-bind:key="cinema.id" :cinema="cinema"/>
                    </div>
                </div>
            </div>
        </section>
    </div>
</div>
</template>

<script>
import Cinema from './Cinema'

export default {
  name: 'CinemaList',
  data() {
    return {
      cinemas: [],
    };
  },
  components:{
    Cinema
  },
  async created(){
    var response = await fetch('http://localhost:8000/api/cinema/');
    this.cinemas = await response.json();
  }
}
</script>