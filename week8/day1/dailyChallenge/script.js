class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}

let video1 = new Video('Introduction to OOP', 'John', 300);
video1.watch();

let video2 = new Video('Advanced JavaScript', 'Jane', 600);
video2.watch();

const videoData = [
    { title: 'Video 1', uploader: 'User1', time: 100 },
    { title: 'Video 2', uploader: 'User2', time: 200 },
    { title: 'Video 3', uploader: 'User3', time: 300 },
    { title: 'Video 4', uploader: 'User4', time: 400 },
    { title: 'Video 5', uploader: 'User5', time: 500 }
];

const videoInstances = videoData.map(data => new Video(data.title, data.uploader, data.time));

videoInstances.forEach(video => video.watch());
