FROM ubuntu:focal
ARG ubuntu_release=focal

RUN groupadd -r user && useradd -r -g user user
# Install ROS Noetic
USER root
RUN apt update
# USER user
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(ubuntu_release) main" > /etc/apt/sources.list.d/ros-latest.list'
# USER root
RUN apt-get update
RUN apt-get install curl -y
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN apt install ros-noetic-desktop-full
RUN apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-rosdep
RUN rosdep init && rosdep update
# Setup environment
USER user
RUN cd ~ && mkdir -p catkin_ws/src
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN source ~/.bashrc && source /opt/ros/noetic/setup.bash &&\
    catkin_make

CMD bash -lc
