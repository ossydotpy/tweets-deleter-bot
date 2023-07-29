Twitter timeline nuke script

this is an extension of [this repo](https://github.com/Mayur57/twitter-nuke/blob/main/src/delete-script.py)

## usage:
1. Obtain your twitter credentials from [twitter](https://developer.twitter.com/en/portal/dashboard)
2. Create a `.env` file in the root directory and paste the content of [env_example](env_example) in there.
3. Edit with our correct credentials. DON'T include the `<>` 
4. Download your Twitter archive from [here](https://twitter.com)
5. Extract the archive
6. Locate the tweets.js file in the data directory.
7. Copy the content between `window.YTD.tweets.part0 = [ ]` and save it in a `tweets.json` file in your root folder.
8. Run `python main.py` and sit back.

