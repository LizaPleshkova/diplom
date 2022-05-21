<template>
    <div>
        <div class="col-sm-12 text-left">
            <div class="container hero-gray-card d-flex align-items-center">
                <div class="container ground-opacity">
                    <div class="col">
                        <div class="row d-flex justify-content-center">
                            <h1>Актуальные забронированные места</h1>
                        </div>
                        <br>
                        <div class="col-sm-12 m-1 text-center " v-if='errorMessage'>
                            <div class="alert alert-warning" role="alert">
                                {{ errorMessage }}
                            </div>
                        </div>
                        <div class="row d-flex justify-content-center" v-if='currentBooking.length != 0'>
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">#</th>
                                        <th scope="col">Киносеанс</th>
                                        <th scope="col">Место</th>
                                        <th scope="col">Цена</th>
                                        <th scope="col">Дата</th>
                                        <th scope="col">Снять бронирование</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <th scope="row"></th>
                                    <tr v-for="(booked, ind) in currentBooking" :key="booked.id">
                                        <td>{{ ind }} {{ booked.id }}</td>
                                        <td>{{ booked.session.movie }}, {{ booked.session.hall }},
                                            {{ booked.session.datetime_session }}
                                        </td>
                                        <td>{{ booked.seat.number_place }} место, {{ booked.seat.number_row }} ряд,
                                           сектор {{ booked.seat.sector }} 
                                        </td>
                                        <td>{{ booked.price }}</td>
                                        <td>{{ booked.datetime_book }}</td>
                                        <td class="d-flex justify-content-center">
                                            <button type="submit" class="btn btn-outline-danger"
                                                v-on:click="deleteBooking(booked.id)">delete</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>

                        </div>
                        <h5 v-else>На данный момент у вас нет заброннированных мест</h5>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-sm-12 text-left">
            <div class="container hero-gray-card d-flex align-items-center">
                <div class="container ground-opacity">
                    <div class="col">
                        <div class="row d-flex justify-content-center">
                            <h1>История забронированных мест</h1>
                        </div>
                        <br>
                        <div class="row d-flex justify-content-center" v-if='historyBooking.length != 0'>
                            <p>
                                Эти данные можно скачать в формате pdf. Для этого нажмите
                                <a href="" class="btn btn-outline-success btn-sm">Downland PDF</a>
                            </p>

                            <div class="row d-flex justify-content-center">
                                <table class="table align-items-center">
                                    <thead>
                                        <tr>
                                            <th scope="col">#</th>
                                            <th scope="col">Киносеанс</th>
                                            <th scope="col">Место</th>
                                            <th scope="col">Цена</th>
                                            <th scope="col">Дата</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(booked, ind) in historyBooking" :key="booked.id" class="justify-content-center align-items-center">

                                            <!-- <th scope="row"></th> -->
                                            <td>{{ booked.id }}</td>
                                            <td>{{ booked.session.movie }}, {{ booked.session.hall }},
                                                {{ booked.session.datetime_session }}
                                            </td>
                                            <td> место {{ booked.seat.number_place }}, {{ booked.seat.number_row }} ряд,
                                               сектор {{ booked.seat.sector }} 
                                            </td>
                                            <td>{{ booked.price }}</td>
                                            <td>{{ booked.datetime_book }} /
                                                {{ booked.datetime_book }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <h5 v-else>На данный момент у вас нет истории заброннрованных мест</h5>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import UserProfileService from "@/services/UserProfile";

export default {
    name: "Profile",
    data() {
        return {
            errorMessage: null,
            idsDeleteBooking: "id" + Math.random().toString(16).slice(2),
        }
    },
    computed: mapGetters(["currentBooking", "historyBooking"]),
    watch: {
        idsDeleteBooking(newIdBooking, oldIdBooking) {
            if (newIdBooking !== oldIdBooking) {
                this.getUserReport();
            }
        }
    },
    methods: {
        ...mapActions(["getUserReport", "deleteBooking"]),
        deleteBooking(pk) {
            console.log(this.newComment);
            console.log("del in profile vue", pk);
            // this.$store.dispatch("deleteBooking", pk);
            UserProfileService.deleteUserBooking(pk).then((report) => {
                console.log("delete booking  ", pk);
                this.idsDeleteBooking = pk.toString() + Math.random().toString(16).slice(2);
                // this.getUserReport(context);
            }).catch(error => {
                this.errorMessage = error.message;
                console.error("There was an error!", error);
                return error;
            });
            console.log("currentBooking")
            const newData = this.currentBooking.filter(item => { console.log(item.id); item.id !== pk; })


            console.log(newData, this.currentBooking)
            this.currentBooking = newData;
            //   this.getUserReport();
        }
    },
    created() {
        console.log("currentBooking", this.currentBooking)
        this.getUserReport();
    },
    mounted() {
        console.log("currentBooking", this.currentBooking)
        this.getUserReport();
    },
};
</script>
