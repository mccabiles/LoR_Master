<template>
    <div class="icon h-7 w-7 xxs:w-8 xxs:h-8 xs:w-9 xs:h-9 sm:h-10 sm:w-10" :class="{champ: code}" :style=" {backgroundImage: getChampionImgUrl}">
        <div v-if="count && count != 3" class="count">{{count}}</div>
    </div>
</template>

<script>

export default {
    components: {

    },
    data() {
        return {
        }
    },
    mounted() {
    },
    props: {
        code: String,
        count: Number,
    },
    computed: {
        getChampionImgUrl() {
            if (!this.code) {
                return "none"
            }
            // const champImageBaseUrl = 'https://raw.githubusercontent.com/painttist/lor-champ-icons/master/images/cards/cropped/';
            // const champImageBaseUrl = 'https://painttist.github.io/lor-champ-icons/images/cards/cropped/';
            // return "url('" + champImageBaseUrl + code + "-cropped.png')"

            // -- Local
            // - v1
            var fileName = this.code + "-cropped.png"
            // return "url('" + cardImages[fileName] + "')"

            // - v2
            return "url(" + require('../../assets/images/cards/cropped/' + fileName) + ")"
        },
    },
    methods: {
    }
}
</script>

<style lang="scss">

    .icon {
        
        display: block;
        margin-right: 0;
        margin-left: 0;
        position: relative;

        padding: 9px;
        text-align: center;
        /* line-height: 30px; */
        /* vertical-align: middle; */
        // width: 18px;
        // height: 18px;
        color: white;

        /* background-color: white; */
        

        background-position: 50% 50%;
        background-size: cover;

        /* background-image: url('../assets/images/cards/cropped/01DE012-cropped.png'); */
    }

    .count {
        position: absolute;
        top: -3px;
        right: -4px;
        font-size: 0.6em;
        padding: 1px 5px;
        border-radius: 100%;

        background: var(--col-light-bg);
        color: var(--cark-white);
    }

    // .won {
    //     .count {
    //         background: var(--col-gold);
    //         color: black;
    //     }
    // }

    .icon.champ {
        border-radius: 30px;
        border: 2px solid rgba(220, 220, 220, 1);
        /* box-shadow: -2px 2px 2px 0px rgba(43, 38, 27, 0.6) inset; */
    }

    /* .icon.champ:hover {
        border: 2px solid rgba(255, 255, 255, 1);
        box-shadow: 1px 2px 5px -2px #000000;
    } */

    // @media screen and (max-width: 275px) {
    //     .icon {
    //         width: 15px;
    //         height: 15px;
    //     }
    // }

    // @media screen and (max-width: 190px) {
    //     .icon {
    //         width: 12px;
    //         height: 12px;
    //     }
    // }

</style>