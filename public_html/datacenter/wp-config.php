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
define( 'DB_NAME', 'dualpower_DataCenter' );

/** MySQL database username */
define( 'DB_USER', 'dualpower_wp1' );

/** MySQL database password */
define( 'DB_PASSWORD', 'hwvBSJ38jUda' );

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
define( 'AUTH_KEY',          'M#R(Cg,_bcF*/_O,gB2+?NFuu]q0!ylV @A<d>]~,JE;TOt;GTm:D ^{gfP*aB*|' );
define( 'SECURE_AUTH_KEY',   'mdY9?+=@0MJ*`KQO36#L-!$0Z*to06e1j^TD43d}HBaf1PMn:nQ:dXb&x]VTMk(P' );
define( 'LOGGED_IN_KEY',     'I0z?~>Vq1tOl0_:zI[B*:M]x&Ak:`UgH_jN+oXe2i:z8OUT)v*Y)J,Q=4YjPFv^(' );
define( 'NONCE_KEY',         'UXZ:h8[##G&ge+p A0Yto&W7:llrH`o<1`K~54Oud/nq,HbegJeG1Tq+&Vnp`xNj' );
define( 'AUTH_SALT',         ';pA|Tr6vZ:o+Op+yl^lhc$|f:V.Jqpwj*h2BQ58[iP+gI.z-;V%J=`4Cfy`?t!tp' );
define( 'SECURE_AUTH_SALT',  '^lHPYrz}Hd@|/6Ka:d/.qw:fx+1+EVJvx|/TzI-$z{/q&|@GhKu;AX1Ud,5y,O7S' );
define( 'LOGGED_IN_SALT',    '*)~h)O/K2RsD4>LX(n6I@a@cUHvLQZBxE2fvcj>P71dLp0WFW _eu*OE(K**%W%w' );
define( 'NONCE_SALT',        '{A7G$ZI#4Ms2uj<>Jnx6M:80K}n/[f{^I.x=`9[VY+:&JgW(|P[[$dP +mPC!lpW' );
define( 'WP_CACHE_KEY_SALT', 'NFKI2-`;SiDx%ZwKoiOVsNOv_T}E(exg~{m|Uq)BKz G0l Ca}@$Y-ZA=I;zz.jx' );

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'dualpower_';




/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) )
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
