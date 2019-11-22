<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'dualpower_wp' );

/** MySQL database username */
define( 'DB_USER', 'dualpower_wp' );

/** MySQL database password */
define( 'DB_PASSWORD', 'qpsw5giMvFVn' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          'siWI;8DHhV%u0eG+$(x5aFYe5u?%QU%=v]KFfeQeso`t8 N)pq.j^f9P`izW4|?6' );
define( 'SECURE_AUTH_KEY',   'u.5f>O683L&:Del7,CpqVZYbBF9]6AD?:Dix#e9)d}xbtne<iMHMsL)Gk|K6m:Bh' );
define( 'LOGGED_IN_KEY',     '`4EB,k%)sNgZZS1gE][aK,~y*;K?`O#W$`PCUBw(q5F94agh.,fKc#>`:{7PtiH0' );
define( 'NONCE_KEY',         'RWl$6^V?1.vv0DBP}==UK6>d&Q3ZQCKnj$SjS.)md.sVQL*QdPbCDk*^2[!D!I&Z' );
define( 'AUTH_SALT',         'X1vLZ}{fxW rt|%1t:YX_OGbruzu.]+`9~&Pl;zP]bWL-?CC2+(%?:vy>4p<h<{E' );
define( 'SECURE_AUTH_SALT',  '/P}w/c}yVDCoXUT(l::Hq>/cc/w8y ,ujn{r/CBP5HK$pp:3J40{C^<3{V)CIWk!' );
define( 'LOGGED_IN_SALT',    'bNx3e[K@0~6eu+Brh8**1W31#;tGgZjmu/Q=0DO,k{$.9?|tM86Nw!`L$3l+dE$%' );
define( 'NONCE_SALT',        'Ekqy7UBtlv_!-2+%<a A_0$Tb!d42C18#nPn}m5Y-x EG_V9X}smVsf(*7:YRGrl' );
define( 'WP_CACHE_KEY_SALT', 'o:*;bL0md@[4Hpi9P(# ^vSW6o2a4Kz^=yZM~}dEaRn^tRe~Z-?9+6jA^1-:Z6@>' );

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';




/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) )
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
