<template>
    <div class="card" >
        <div class="card-body text-center">
        
    <img v-bind:src="cinema.image" alt="" class="card-img-top">
            <h5 class="card-title ">{{ cinema.name }}</h5>
            <div class="card-text">
            <p >{{ cinema.address }}</p>
            <p >{{ cinema.phone_number }}</p>
            </div>
            
    <router-link :to="{ name: 'cinema-detail', query: { id: cinema.id }}" 
                class="btn btn-outline-success btn-sm">Read More </router-link>

        </div>
    </div>
                    
</template>

<script>
export default {
  name: 'Cinema',
  props:{
      cinema:{
          type:Object,
          default:()=>{}
      }
  },
//   created() {
//     const cinema = cinemas.find(cinema => cinema.id == this.$route.params.id)
//     if (cinema) {
//       this.cinema = cinema
//     }
//   }


}
</script>