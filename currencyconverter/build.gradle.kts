plugins {
    id("java")
}

group = "org.skdesign"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.8.1")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.8.1")
    implementation("com.squareup.okhttp3:okhttp:3.14.6")
}

tasks.getByName<Test>("test") {
    useJUnitPlatform()
}