

if __name__ == "__main__":
    from multiprocessing import Queue, Process
    from game_engine import game
    from imagetrack import hand_tracker

    queue = Queue()

    game_p = Process(target=game, args=(queue,))
    hand_tracker_p = Process(target=hand_tracker, args=(queue,))

    hand_tracker_p.start()
    game_p.start()

    game_p.join()

    if hand_tracker_p.is_alive():
        hand_tracker_p.terminate()
