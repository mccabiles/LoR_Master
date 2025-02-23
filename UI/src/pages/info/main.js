import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'

import App from './Info.vue'
import '@/assets/css/global.css'

import { createStore, mapState, mapMutations } from 'vuex'

const store = createStore({
  state () {
    return {
      locale: 'en_us',
      IS_ELECTRON: window.ipcRenderer !== undefined,
    }
  },
  mutations: {
    changeLocale (state, newLocale) {
        state.locale = newLocale
    }
  }
})

const messages = require('@/assets/data/messages.js')

const i18n = createI18n({
  locale: 'English', // set locale
  fallbackLocale: 'English', // set fallback locale
  messages,
})

const app = createApp(App)

app.use(i18n).use(store)

app.mixin({
  computed: {
    ...mapState([
      'locale',
      'IS_ELECTRON'
    ])
  },
  methods: {
    ...mapMutations([
      'changeLocale'
    ]),
  }
})

app.mount('#app')