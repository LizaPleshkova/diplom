<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
      <div class="col-12 col-md-7">
        <div class="card p-3">
          <div class="row">
            <div class="col-12 col-md-7">
              <img
                v-bind:src="cinema.image"
                alt=""
                class="m-2 card-img-left"
                height="300"
                width="425"
              />
            </div>
            <div class="col-12 col-md-5 py-3 px-4">
              <p class="small font-weight-bold my-2">cinema</p>
              <h3 class="mb-3">
                {{ cinema.name }}
              </h3>
              <p>
                <strong>Address: </strong>{{ cinema.address }}<br />
                <strong>Phone number: </strong>{{ cinema.phone_number }}<br />
              </p>
              <div class="d-flex mb-3">
                <small class="text-muted">
                  <router-link
                    :to="{
                      name: 'cinema-detail',
                      params: { cinemaId: cinema.id },
                    }"
                  >
                    here you can view movie sessions
                  </router-link></small
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Cinema",
  props: ["cinema"],
};
</script>
