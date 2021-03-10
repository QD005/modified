from instapy import InstaPy
import schedule
import os.path
import time
def job():
    session = InstaPy(username="clickhustlers", password="Backsp@c5", headless_browser=True)
    session.login()
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                  peak_likes_hourly=57,
                                  peak_likes_daily=585,
                                   peak_comments_hourly=21,
                                   peak_comments_daily=182,
                                    peak_follows_hourly=48,
                                    peak_follows_daily=None,
                                     peak_unfollows_hourly=35,
                                     peak_unfollows_daily=402,
                                      peak_server_calls_hourly=None,
                                      peak_server_calls_daily=4700)
    session.set_relationship_bounds(enabled=True,
                     potency_ratio=1.34,
                      delimit_by_numbers=True,
                       max_followers=8500,
                        max_following=4490,
                         min_followers=100,
                          min_following=56,
                           min_posts=10,
                    max_posts=1000)                                  
    session.set_delimit_liking(enabled=True, max_likes=999, min_likes=20)                                 
    session.like_by_tags(["photography", "art", "lifestyle"], amount=5)
    session.set_relationship_bounds(enabled=True, max_followers=5000)
    session.set_do_follow(True, percentage=50, times=True)
    directory= os.path.dirname(os.path.realpath(__file__))
    filename = "users.txt"          
    file_path = os.path.join(directory,'files/', filename)
    users = session.target_list(file_path)
    session.follow_likers(users, randomize=False)
    session.set_delimit_commenting(enabled=True, max_comments=32, min_comments=0)
    session.set_do_comment(True, percentage=50)
    
    session.set_comments(["Nice!","Really nice","so quite","Sweet!", "Awesome", "really cool", "i like your stuff", "Lovely", "adorable", "Beautiful"])
    # Prevents unfollow followers who have liked one of your latest 5 posts
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.unfollow_users(amount=10, delay_followbackers=604800)
    session.end()
job()
#schedule.every().day.at('8:15').do(job)
#while True:
#    schedule.run_pending()
#    time.sleep(15)

# Follow the followers of each given user
       