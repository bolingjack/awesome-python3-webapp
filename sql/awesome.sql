/*
 Navicat MySQL Data Transfer

 Source Server         : AWS数据库测试
 Source Server Type    : MySQL
 Source Server Version : 50635
 Source Host           : yuyingqi-develop.cszis4r93tw8.rds.cn-north-1.amazonaws.com.cn
 Source Database       : awesome

 Target Server Type    : MySQL
 Target Server Version : 50635
 File Encoding         : utf-8

 Date: 02/01/2018 13:55:33 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `blogs`
-- ----------------------------
DROP TABLE IF EXISTS `blogs`;
CREATE TABLE `blogs` (
  `id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `summary` varchar(200) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `comments`
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` varchar(50) NOT NULL,
  `blog_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
