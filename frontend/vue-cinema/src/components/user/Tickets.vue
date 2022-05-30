<template>
    <div class="col-sm-12 container-fluid mx-auto">
        
        <div class="row  justify-content-around m-1 p-1">
            {{ selectedBookingIds }}
            <!-- Может сделать форма для отправки на почту(она ведь может оличаться от исходной при регистраии) -->
            <button class="btn btn-outline-success btn-sm-2  m-1 p-1" @click="">Send to email</button>
            <button class="btn btn-outline-success btn-sm-2  m-1 p-1" @click="generateReport">Download in PDF</button>
        </div>
            <section slot="pdf-content"  ref="document">
                <div class="row justify-content-around">
                    <section class="container">
                        <div v-for="(booked, ind) in Bookings" :key="booked.id">
                            <article class="card fl-left m-1 p-1">
                                <section class="date">
                                    <time datetime="23th feb">
                                        <!-- here will be qr -code -->
                                        <vue-qrcode v-bind:value="booked.id_ticket" />
                                    </time>
                                </section>
                                <section class="card-cont">
                                    <small>cinema {{ booked.cinema.name }}</small>
                                    <h3>{{ booked.session.movie }}</h3>
                                    <div class="even-date">
                                        <i class="fa fa-calendar"></i>
                                        <time>
                                            {{ booked.seat.number_place }}seat, {{ booked.seat.number_row }} row, {{
                                                    booked.seat.sector
                                            }}
                                            sector, {{ booked.price }} price

                                            <span>{{ booked.session.datetime_session }}</span>
                                        </time>
                                    </div>
                                    <div class="even-info">
                                        <i class="fa fa-map-marker"></i>
                                        <p>
                                            CINEMA ADDRESS {{ booked.cinema.address }}
                                            CINEMA PHONE NUMBER {{ booked.cinema.phone_number }}
                                        </p>
                                    </div>
                                    <a href="#">booked</a>
                                </section>
                            </article>
                        </div>
                    </section>
                </div>
            </section>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import VueQrcode from 'vue-qrcode'
import Vue3Html2pdf from 'vue3-html2pdf'
import * as html2pdf from 'html2pdf.js'
import * as html2canvas from 'html2canvas'

export default {
    name: "Ticket",
    components: {
        VueQrcode,
        Vue3Html2pdf
    },
    data() {
        return {
            errorMessage: null,

        };
    },
    props: ['selectedBookingIds'],
    computed: mapGetters(["Bookings", "ticketsFile"]),
    methods: {
        ...mapActions(["getUserBookedTickets", "downloadTickets"]),
        downloadTickets() {
            this.downloadTickets();
        },
        generateReport() {
            console.log('here')
            // this.$refs.html2Pdf.generatePdf()
            html2pdf(this.$refs.document, {
        margin: 0.2,
        filename: "new.pdf",
        // pagebreak:  { after: '.sautDePage' },
       
        html2canvas: { 
          scale: 2, 
          letterRendering: true
        },
        jsPDF: { 
          unit: "in", 
          format: "a4", 
          orientation: "portrait"
        },
      });
        }
    },
    created() {
        console.log("from MD", this.$route.params.selectedBookingIds);
        // this.$store.dispatch.getUserBookedTickets(this.$route.params.selectedBookingIds);
        this.getUserBookedTickets(this.$route.params.selectedBookingIds);
        // this.getUserBookedTickets(['233']);
    },
    mounted() {
      let recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', 'html2pdf.bundle.min.js')
      document.head.appendChild(recaptchaScript)
    },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Oswald');

* {
    margin: 0;
    padding: 0;
    border: 0;
    box-sizing: border-box
}

body {
    background-color: #dadde6;
    font-family: arial
}

.fl-left {
    float: left
}

.fl-right {
    float: right
}

h1 {
    text-transform: uppercase;
    font-weight: 900;
    border-left: 10px solid #fec500;
    padding-left: 10px;
    margin-bottom: 30px
}

.row {
    overflow: hidden
}

.card {
    display: table-row;
    width: 49%;
    background-color: #fff;
    color: #989898;
    margin-bottom: 10px;
    font-family: 'Oswald', sans-serif;
    text-transform: uppercase;
    border-radius: 4px;
    position: relative
}

.card+.card {
    margin-left: 2%
}

.date {
    display: table-cell;
    width: 25%;
    position: relative;
    text-align: center;
    border-right: 2px dashed #dadde6
}

.date:before,
.date:after {
    content: "";
    display: block;
    width: 30px;
    height: 30px;
    background-color: #DADDE6;
    position: absolute;
    top: -15px;
    right: -15px;
    z-index: 1;
    border-radius: 50%
}

.date:after {
    top: auto;
    bottom: -15px
}

.date time {
    display: block;
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%)
}

.date time span {
    display: block
}

.date time span:first-child {
    color: #2b2b2b;
    font-weight: 600;
    font-size: 250%
}

.date time span:last-child {
    text-transform: uppercase;
    font-weight: 600;
    margin-top: -10px
}

.card-cont {
    display: table-cell;
    width: 75%;
    font-size: 85%;
    padding: 10px 10px 30px 50px
}

.card-cont h3 {
    color: #3C3C3C;
    font-size: 130%
}

.row:last-child .card:last-of-type .card-cont h3 {
    text-decoration: line-through
}

.card-cont>div {
    display: table-row
}

.card-cont .even-date i,
.card-cont .even-info i,
.card-cont .even-date time,
.card-cont .even-info p {
    display: table-cell
}

.card-cont .even-date i,
.card-cont .even-info i {
    padding: 5% 5% 0 0
}

.card-cont .even-info p {
    padding: 30px 50px 0 0
}

.card-cont .even-date time span {
    display: block
}

.card-cont a {
    display: block;
    text-decoration: none;
    width: 80px;
    height: 30px;
    background-color: #D8DDE0;
    color: #fff;
    text-align: center;
    line-height: 30px;
    border-radius: 2px;
    position: absolute;
    right: 10px;
    bottom: 10px
}

.row:last-child .card:first-child .card-cont a {
    background-color: #037FDD
}

.row:last-child .card:last-child .card-cont a {
    background-color: #F8504C
}

@media screen and (max-width: 860px) {
    .card {
        display: block;
        float: none;
        width: 100%;
        margin-bottom: 10px
    }

    .card+.card {
        margin-left: 0
    }

    .card-cont .even-date,
    .card-cont .even-info {
        font-size: 75%
    }
}
</style>
