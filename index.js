const axios = require("axios")
const endpoint = "https://graph.facebook.com/"

async function getAccessToken(appId, appSecret) {
    const url = `oauth/access_token?client_id=${appId}&client_secret=${appSecret}&grant_type=client_credentials`
    const result = await axios.get(`${endpoint}/${url}`)
    console.log(result.data)
}

async function getUserInfoAndPosts(instagramAccountId, username, endpoint, accessToken) {
    const url = `me?fields=id,
    name,
    name_format,
    picture,
    permissions,
    email,
    first_name,
    last_name,
    install_type,
    installed,
    is_guest_user,
    short_name,
    supports_donate_button_in_live_video,
    video_upload_limits
    &access_token=${accessToken}`
    

    const result = await axios.get(`${endpoint}/${url}`)

    console.log(result.data)
    }

getUserInfoAndPosts("24024368050510398", "kishammel", endpoint, "EAAW94TgHvDIBOw4R2ZCh20wlsNFBPXotZBvA8WPRWM06xKjPnCmvlRE5h2gT0QUuU3JnZCDPSNfBitwxCAyl31BQMB3rowcCM7LlzvollL9LVuI5WR1q3R2K2qwKTALGuSEtCGF5oaqHQpt10S8oawxRoZAsTIKHgkFUI3vvcW70IxH7SLqpPuTsSCweUwSwzLRDQZBfjEoxgkcbZBAZAdpG7NMAnWuUzOksQfm0rZCPrZAK3W8Yb0ZC23RYREfta1TgZDZD")