<template>
    <div class="icon-container gap-0.5 sm:gap-1 p-0 sm:p-1">
        <champ-icon v-for="(champ, index) in getChamps" :key="index" :code="champ.code" :count="champ.count"></champ-icon>
        <div class="extra-champ" :class="{'fixed-width': fixedWidth }" v-if="extraChampString">{{extraChampString}}</div>
        <deck-regions v-if="getChamps.length <= 0 && showRegion" :deck="deck" :fixedWidth="fixedWidth"></deck-regions>
    </div>
</template>

<script>

import DeckEncoder from '../../modules/runeterra/DeckEncoder'
import championCards from '../../assets/data/champion.js'
import ChampIcon from '../image/ChampIcon.vue'
import DeckRegions from './DeckRegions.vue'

// const maxChamp = 2;

export default {
    components: { ChampIcon, DeckRegions },
    data() {
        return {}
    }, 
    mounted() {
    },
    props: {
        deck: {
            type: String,
            require: true
        },
        maxChamp: {
            type: Number,
            default: 2
        },
        showRegion: {
            type: Boolean,
            default: false
        },
        fixedWidth: {
            type: Boolean,
            default: true
        }
    },
    computed: {
        getChamps() {
            return this.getChampsFromDeck.slice(0, this.maxChamp)
        },
        extraChampString() {
            var extra = (this.getChampsFromDeck.length - this.maxChamp)
            if (extra > 0)
                return "+" + extra
            return ""
        },
        getChampsFromDeck() {
            var deck = null

            // this.$store.dispatch('getData')
            let cache = this.$store.getters.champsFromDeck[this.deck]
            if (cache) {
                return cache
            }

            try { deck = DeckEncoder.decode(this.deck)} catch(err) {
                console.log(err)
                console.log(this.deck)
                return []
            }
            var champs = []
            for (var j in deck) {
                let champCode = deck[j].code
                if (championCards.champObj[champCode] != null) {
                    let champ = {
                        count: deck[j].count,
                        code: champCode
                    }
                    champs.push(champ)
                }
                // for (var i in championCards.champions) {
                //     var champCode = championCards.champions[i]
                //     var cardCode = deck[j].code
                //     if (cardCode == champCode) {
                //         let champ = {
                //             count: deck[j].count,
                //             code: champCode
                //         }
                //         champs.push(champ)
                //     }
                // }
            }
            champs = champs.sort((a, b) => a.code > b.code ? 1 : -1)
            this.$store.dispatch('addChampsFromDeck', {champs: champs, deckCode: this.deck})
            // Add filler champ icons
            
            if (this.fixedWidth) {
                var fillerIcons = this.maxChamp - champs.length
                for (let i = 0; i < fillerIcons; i++) {
                    let champ = {
                        count: null,
                        code: null
                    }
                    // Return a deep copy so the stored cache is not modified
                    var filledChamps = champs.map(a => ({...a}));
                    filledChamps.push(champ)
                    return filledChamps
                }
            }
            return champs
        },
    },
    methods: {
    }
}
</script>

<style>

    .icon-container {
        display: flex;
        gap: 2px;
        /* padding: 4px; */
        align-items: center;
        position: relative;

        /* border-radius: 50px; */
    }
    
    .btn:hover .icon-container .icon.champ,
    .btn.active .icon-container .icon.champ {
        border: 2px solid rgba(255, 255, 255, 1);
        box-shadow: 1px 2px 5px -2px #000000;
    }

    .icon {
        border: 2px solid transparent;
    }

    .extra-champ.fixed-width {
        position: absolute;
        bottom: -3px;
        right: -7px;
        /* background: var(--col-background); */
        border-radius: 5px;
    }

    /*     
    .count {
        padding: 2px;
        background: var(--col-darker-grey);
        border-radius: 100%;
    } */

</style>